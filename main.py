import engine
import views

engine.init([500, 500])

exit_button = engine.components.button.Button('EXIT!', 100, 100)

engine.start_game(views.TitleScreen(
    exit_button
))
