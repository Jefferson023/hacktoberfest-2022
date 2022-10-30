public class Question2 {

    Integer hora;

    Double salario;

    Double salario_final;


    public Question2(Integer horasTrabalhadas, Double salarioAtual){
        this.hora = horasTrabalhadas;
        this.salario = salarioAtual;
        calcularSalario();
    }

    private void calcularSalario(){
        this.salario_final = salario + ((hora - 40)+( salario*0.50));   
    }

    public void render(){
        System.out.println("======= SALARIO FINAL ========");
        System.out.println("R$: "+this.salario_final);
    }
}
