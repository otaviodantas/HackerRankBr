// hackerrank.com/challenges/angry-professor
// score: 20

string angryProfessor(int k, vector<int> a){
  int count = 0;
  for(int x:a){
    if(x <= 0) ++count;

    if(count >= k) return "NO";
  }
  return "YES";
}
