from app import create_app



application = create_app()


if __name__ == "main":
    application.run(host="0.0.0.0", port="8080")
