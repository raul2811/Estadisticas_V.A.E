import reflex as rx

config = rx.Config(
    app_name="vae",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)