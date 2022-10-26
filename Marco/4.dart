void main(){
  int num1 = 6;
  int num2 = 1;
  int num3 = 3;
  
  print(bogoSort([num1,num2,num3]));
}

List<int> bogoSort(List<int> num){
  while(!check(num)){
    num.shuffle();
  }
  return num;
}

bool check(List<int> num){
  for(var i = 0; i < num.length-1; i++){
    if(num[i] > num[i+1]){
      return false;
    }
  }
  return true;
}
