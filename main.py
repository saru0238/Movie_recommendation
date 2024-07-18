import Recommendation_algo as rec

while True:
    print("1- recommend movie\n2- exit")
    ch = input("Enter choice: ")

    if ch=='1':
        movie=input('Enter Movie Name: ')

        index=rec.index_from_movie(movie)
        if index is None:
            print("Movie not found in database")
            break
            

        rec_movie_index=rec.recomn_fn(index)

        rec_movie=rec.movie_from_index(rec_movie_index)

        print(f'Our Recommendation is: {rec_movie}' )

    else:
        break
