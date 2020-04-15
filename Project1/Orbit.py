from discord import Webhook, RequestsWebhookAdapter, Embed, Color
def avatar_url():
    return'https://images-ext-1.discordapp.net/external/bFAefuOEByo1ZRhjLY-6tQzDMcu_7D7lCcNfgvNpnVE/https/i.ibb.co/xD2v5wF/orbitboteu-logo.png'
def product_url():
    return 'https://cdn.discordapp.com/attachments/693035028405420133/696244120632426536/H67799.png'
def send_webhook():
    url = 'https://discordapp.com/api/webhooks/699902394187644940/Yxx0wyI0N6B6e5ydrpw5gxsnyBSg0G2w7s0xrtFmca35Jhc7hlSoi50V4u2IeiO6ZLnU'
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

    embed = Embed(title='Yeezy 700 V3"Alvah"',
                  url="https://twitter.com/orbitboteu",
                  color=Color.from_rgb(67, 194, 122))

    embed.set_thumbnail(url=product_url())

    embed.add_field(name="Srore", value="Holypopstore")\
        .add_field(name="profile", value="||test||")\
        .add_field(name="size", value="9")
    embed.add_field(name="Payment Method", value="Paypal")\
        .add_field(name="Account", value="||test@test.com||")\
        .add_field(name="Timestamp", value="||2020-03-31 13:00:16PM(UTC)||", inline=False)
    embed.set_footer(text='Orbit', icon_url=avatar_url())

    embed.set_author(name="Successfully checked out!")

    webhook.send(embed=embed, avatar_url=avatar_url(), username="Orbit Success")

send_webhook()