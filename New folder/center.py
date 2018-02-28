import fresh_tomatoes
import media
toy_story = media.movie('toy story', 'a boys toy comes to life', 'https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450', 'https://www.youtube.com/watch?v=4KPTXpQehio')

#print (toy_story.poster_image_url)
avatar = media.movie('avatar', 'fucking allians', 'http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp','https://www.youtube.com/watch?v=5PSNL1qE6VY')
#avatar.show_trailer()
wind_river = media.movie('wind river', 'A veteran tracker with the Fish and Wildlife Service helps to investigate the murder of a young Native American woman, and uses the case as a means of seeking redemption for an earlier act of irresponsibility which ended in tragedy.', 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyMjU1OTUwM15BMl5BanBnXkFtZTgwMDg1NDQ2MjI@._V1_UX182_CR0,0,182,268_AL_.jpg', 'https://www.youtube.com/watch?v=zN9PDOoLAfg')
#wind_river.show_trailer()
movies = [avatar,wind_river ,toy_story]
fresh_tomatoes.open_movies_page(movies)