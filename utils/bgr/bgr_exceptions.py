class ResponseConnectionError(Exception):
    """An exception raised when a connection error occurs during HTTP connection."""

    def __init__(self):
        super().__init__("Connection error occurred.")


class ResponseContentError(Exception):
    """An exception raised when an error occurs while reading an HTTP response."""

    def __init__(self):
        super().__init__("Could not retrieve Response Content.")


class UnsupportedFileType(Exception):
    """An exception raised when an unsupported file type is detected."""

    def __init__(self, mime_type: str):
        msg = "Detected file mime type as: " f"'{mime_type}', which is not supported."
        super().__init__(msg)


class ContextAttachmentUnavailable(Exception):
    """
    An exception raised when an error occurs
    if attachment url is not present in Context.
    """

    def __init__(self):
        super().__init__("Could not retrieve attachment URL.")


class ImageError(Exception):
    """An exception raised when an error occurs upon loading an image."""

    def __init__(self):
        msg = "An error occurred while loading the image."
        super().__init__(msg)


class ImageDecompositionError(Exception):
    """An exception raised when an error occurs in AnimatedDecompose."""

    def __init__(self):
        msg = "An error occurred while decomposing the image."
        super().__init__(msg)


class VideoDecompositionError(Exception):
    """An exception raised when an error occurs in VideoDecompose."""

    def __init__(self):
        msg = "An error occurred while decomposing the video."
        super().__init__(msg)


class ExceedsMaxFrames(Exception):
    """
    An exception raised when a video or animated file
    exceeds a specified frames limit.
    """

    def __init__(self, fp_format: str, num_frames: int, max_frames: int):
        msg = (
            f"{fp_format} exceeds maximum of {max_frames} frames.\n"
            f"Frame Count: {num_frames}"
        )
        super().__init__(msg)


class ExceedsMaxResolution(Exception):
    """An exception raised when a media file exceeds a specified maximum resolution."""

    def __init__(self, fp_format: str, width: int, height: int, max_px: int):
        msg = (
            f"{fp_format.upper()} needs to be <{max_px}px in width or height.\n"
            f"Resolution: {width}x{height}"
        )
        super().__init__(msg)


class SubceedsMinResolution(Exception):
    """An exception raised when a media file subceeds a specified minimum resolution."""

    def __init__(self, fp_format: str, width: int, height: int, min_px: int):
        msg = (
            f"{fp_format.upper()} needs to be >{min_px}px in width or height.\n"
            f"Resolution: {width}x{height}"
        )
        super().__init__(msg)


BGR_EXCEPTIONS = (
    ResponseConnectionError,
    ResponseContentError,
    UnsupportedFileType,
    ContextAttachmentUnavailable,
    ImageError,
    ImageDecompositionError,
    VideoDecompositionError,
    ExceedsMaxFrames,
    ExceedsMaxResolution,
    SubceedsMinResolution,
)
