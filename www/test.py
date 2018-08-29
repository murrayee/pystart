import orm,asyncio
from models import User,Blog,Comment

async def test(loop):
    await orm.create_pool(loop,user='root',password='12345678',db='awesome')
    u = User(name='Jiaxi1n Li',email='murray1ee@163.com',passwd='12341567890',image='about:blank')
    await u.save()

async def find(loop):
    await orm.create_pool(loop,user='root',password='12345678',db='awesome')
    rs = await User.findAll()
    print('查找测试： %s' % rs)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([test(loop),find(loop)]))
loop.run_forever()
