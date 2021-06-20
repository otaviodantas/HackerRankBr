// hackerrank.com/challenges/strange-advertising/
// score: 15

func viralAdvertising(n int32) int32 {
    population := 5
    count := 0
    s_pop := 0
    
    for i := 0; i < int(n); i++ {
        s_pop = population / 2
        count += s_pop
        population = s_pop * 3
    }
    
    return int32(count)
    
}
