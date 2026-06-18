from random import randint

import discord
from bd_models.models import Player, Special
from ..models import SpecialBonuses
from django.db.models import Count, Q
from ballsdex.core.bot import BallsDexBot
from ballsdex.settings import settings
from ballsdex.packages.countryballs.countryball import BallSpawnView


async def monkeypatch(bot: "BallsDexBot"):
    from typing import cast
    from ballsdex.packages.countryballs import CountryBallsSpawner
    cog = cast("CountryBallsSpawner", bot.get_cog("CountryBallsSpawner"))
    if cog is None:
        return
    class BallSpawnViewOverride(BallSpawnView):
        async def catch_ball(
            self,
            user: discord.User | discord.Member,
            *,
            player: Player | None,
            guild: discord.Guild | None,
        ):
            ball, is_new = await super().catch_ball(user, player=player, guild=guild)

            bonus = await SpecialBonuses.objects.filter(
                special=ball.special
            ).afirst()

            if bonus:
                hb = randint(
                    int(bonus.bonus * 0.95),
                    int(bonus.bonus * 1.05),
                )
                ab = randint(
                    int(bonus.bonus * 0.95),
                    int(bonus.bonus * 1.05),
                )
                ball.health_bonus += hb
                ball.attack_bonus += ab
                await ball.asave(update_fields=["health_bonus", "attack_bonus"])

            return ball, is_new

    cog.countryball_cls = BallSpawnViewOverride

    cog.countryball_cls = BallSpawnViewOverride
