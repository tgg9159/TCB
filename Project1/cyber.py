from discord import Webhook, RequestsWebhookAdapter, Embed, Color
def avatar_url():
    return'https://cdn.discordapp.com/avatars/650665273053151239/b63669f142e713de30f1f5f48b33502d.webp?size=128'
def product_url():
    return 'https://images-ext-2.discordapp.net/external/NrbSEa1_rLDwnfNPp0co9FmjfNfbAgjyL6GVSDyhnqY/https/assets.supremenewyork.com/186849/rs/k9sHDyYfhIs.jpg?width=450&height=450'
def send_webhook():
    url = 'https://discordapp.com/api/webhooks/699902394187644940/Yxx0wyI0N6B6e5ydrpw5gxsnyBSg0G2w7s0xrtFmca35Jhc7hlSoi50V4u2IeiO6ZLnU'
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(title='Successfully checked out!',
                  color=Color.from_rgb(50, 205, 50),
                  description='Tupac Hologram Tee')

    embed.set_thumbnail(url=product_url())

    embed.add_field(name='Store', value='Supreme EU', inline=True)\
        .add_field(name='size', value='XLarge', inline=True)\
        .add_field(name='Profile', value='||test||', inline=True)

    embed.add_field(name='Order', value='||4567891||', inline=True)\
        .add_field(name='Proxy List', value='||test||', inline=True)\
        .add_field(name='Color', value='black', inline=True)

    embed.add_field(name='Category', value='T-Shirts', inline=True)\
        .add_field(name='3D Secure', value='Enabled', inline=True)\
        .add_field(name='Mode', value='Safe', inline=True)

    embed.set_footer(text='CyberAIO•27/02/2020 16:03:37.984', icon_url=avatar_url())

    webhook.send(embed=embed, avatar_url=avatar_url(), username="CyberAIO")
send_webhook()
