void main(){
  int num1 = 2;
  int num2 = 1;
  int num3 = 3;
  
  print(checkTriangle([num1,num2,num3]));
}

bool checkTriangle(List<int> num){
  assert(num.length == 3);
  if(num[0] > (num[1] + num[2])){
    return false;
  } else if(num[1] > (num[0] + num[2])){
    return false;
  } else if(num[2] > (num[0] + num[1])){
    return false;
  }
  return true;
}
