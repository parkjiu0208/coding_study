def solution(genres, plays):
    genre_map = dict()
    for i in range(len(genres)):
        if genres[i] not in genre_map:
            genre_map[genres[i]] = 0
        genre_map[genres[i]] += plays[i] 
        
    items = [(-genre_map[genres[i]], -plays[i], i) 
             for i in range(len(genres))]
    items.sort()
    
    album = []
    la_gen = ''
    cnt = 0
    for item in items:
        if la_gen == genres[item[2]]:
            count += 1
        else:
            count = 1
        la_gen = genres[item[2]]
        if count > 2: 
            continue
        album.append(item[2])
    return album