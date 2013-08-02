#!/var/www/musicvideo/env/bin/python

# importing all crawling scripts
from sparkups import sparkups_crawler
from gorillavsbear import gorillavsbear_crawler
from portals import portals_crawler
from yvynyl import yvynyl_crawler
from disconaivete import disco_naivete_crawler
from iguessimfloating import iguessimfloating_crawler
from lostlostlost import lostlostlost_crawler
from sonicmasala import sonicmasala_crawler
from stadiumsandshrines import stadiumsandshrines_crawler
from blogotheque import blogotheque_crawler
from smokedontsmoke import smoke_dont_smoke_crawler

# calling all crawling scripts

sparkups_crawler()
gorillavsbear_crawler()
portals_crawler()
yvynyl_crawler()
disco_naivete_crawler()
iguessimfloating_crawler()
lostlostlost_crawler()
sonicmasala_crawler()
stadiumsandshrines_crawler()
blogotheque_crawler()
smoke_dont_smoke_crawler()
