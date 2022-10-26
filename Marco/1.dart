void main(){
  int num1 = 4;
  int num2 = 5;
  int num3 = 6;
  
  print(calcMedia([num1,num2,num3]));
}

int calcMedia(List<int> num){
  int temp = 0;
  for(var n in num){
    temp += n;
  }
  
  return (temp/num.length).round();
}
