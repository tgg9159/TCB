from discord import Webhook, RequestsWebhookAdapter, Embed, Color
def avatar_url():
    return'https://cdn.discordapp.com/avatars/650665273053151239/b63669f142e713de30f1f5f48b33502d.webp?size=128'
def pround_url():
    return 'https://images.footlocker.com/pi/54724069/cart/54724069.jpeg'
def send_webhook(content):
    url = 'https://discordapp.com/api/webhooks/699902394187644940/Yxx0wyI0N6B6e5ydrpw5gxsnyBSg0G2w7s0xrtFmca35Jhc7hlSoi50V4u2IeiO6ZLnU'
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

    embed = Embed(title="You cooked", color=10181046)\
        .set_thumbnail(url=pround_url())

    embed.add_field(name="Website", value="Eastbay")\
        .add_field(name="Product", value="Jordan AJ 1 Mid - Men's")\
        .add_field(name='Size', value='||6||')

    embed.add_field(name='Price', value="$115.00")\
        .add_field(name='Link', value="54724069")\
        .add_field(name='Profile', value="||test||")

    embed.add_field(name='Proxy', value="||127.0.0.1:33128||")\
        .add_field(name='Time stamp (utc)', value="2020-03-31 13:00:16PM")

    webhook.send(content, embed=embed)

send_webhook("Success: Jordan AJ 1 Mid - Men's")