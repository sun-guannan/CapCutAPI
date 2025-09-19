from flask import Flask


def register_blueprints(app: Flask) -> None:
    """Register all API blueprints on the given Flask app."""
    from .video import bp as video_bp
    from .audio import bp as audio_bp
    from .image import bp as image_bp
    from .text import bp as text_bp
    from .subtitle import bp as subtitle_bp
    from .sticker import bp as sticker_bp
    from .effects import bp as effects_bp
    from .drafts import bp as drafts_bp
    from .metadata import bp as metadata_bp
    from .generate import bp as generate_bp
    from .health import bp as health_bp
    from .tasks import bp as tasks_bp
    from .draft_management_api import draft_bp as draft_management_bp

    # No url_prefix to preserve existing routes
    app.register_blueprint(video_bp)
    app.register_blueprint(audio_bp)
    app.register_blueprint(image_bp)
    app.register_blueprint(text_bp)
    app.register_blueprint(subtitle_bp)
    app.register_blueprint(sticker_bp)
    app.register_blueprint(effects_bp)
    app.register_blueprint(drafts_bp)
    app.register_blueprint(metadata_bp)
    app.register_blueprint(generate_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(draft_management_bp)

