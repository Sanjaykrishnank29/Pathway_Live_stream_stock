import logging
import time
from typing import Dict, List, Callable
from functools import wraps

logger = logging.getLogger(__name__)


def retry_llm_call(max_retries: int = 3, initial_delay: float = 1.0):
    """
    Decorator for retrying LLM calls with exponential backoff.
    """

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            delay = initial_delay
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries == max_retries:
                        logger.error(f"Max retries reached for LLM call: {e}")
                        raise
                    logger.warning(
                        f"LLM call failed (attempt {retries}/{max_retries}): {e}. Retrying in {delay}s..."
                    )
                    time.sleep(delay)
                    delay *= 2
            return None

        return wrapper

    return decorator


def create_esg_prompt(company: str, esg_score: int) -> List[Dict[str, str]]:
    """
    Creates a standardized prompt for ESG analysis.
    """
    return [
        {
            "role": "user",
            "content": (
                f"As an ESG expert, analyze the sustainability efforts of {company} "
                f"which has an ESG score of {esg_score}. Provide a concise 2-sentence insight."
            ),
        }
    ]
