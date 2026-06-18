# SpecialBonuses
Adds special bonuses for BallsDex! You can configure bonuses inside the admin panel.
## Installation
1. Put this into `config/extra.toml`
   ```toml
   [[ballsdex.packages]]
   location = "git+https://github.com/cewlgruyere/SpecialBonuses.git"
   path = "SpecialBonuses"
   enabled = true
   ```
2. Rebuild the bot.
   do:  
   ```
   docker compose build
   docker compose up
   ```
## How2Use (a not so good guide)
Firstly, after installing and starting it, go to the admin panel and select Special Bonuses. When you are in the special bonuses tab, press new and select a special as well as the bonus. there is a 10% gap (like if you select 1000 it would be between 900-1100). After that idrk if it works just after or if you need to reloadcache but figure it out ig.  
It monkeypatches the original catch_ball function so it should work fine. If you already have a bunch of people with specials just create a dbeval or sum shit