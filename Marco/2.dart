void main(){
  int saldo = 2;
  int debito = 1;
  int credito = 3;
  
  var saldoAtual = (checkSaldo(saldo,debito,credito));
  
  if(saldoAtual < 0){
    print("Saldo Negativo");
  }
  else{
    print("Saldo positivo");
  }
}

int checkSaldo(int saldo, int debito, int credito){
  return saldo-(debito+credito);
}
