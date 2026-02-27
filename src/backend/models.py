import pathway as pw


class GreenAssetSchema(pw.Schema):
    """Schema for incoming green asset data stream."""

    company: str
    esg_score: int
