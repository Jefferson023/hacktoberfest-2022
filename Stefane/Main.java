import java.util.Random;

public class Main {

    public static void TestQuestionOne(){
        Random gerador = new Random();

        for(int i = 0; i < 10; i++){
            Question1 question1 = new Question1("Aluno "+i, gerador.nextInt(11)+0.0,gerador.nextInt(11)+0.0,gerador.nextInt(11)+0.0);
            question1.processSituacaoFinal();
            question1.render();
        }  
    }

    public static void TestQuestionTwo(){
        Random gerador = new Random();

        for(int i = 0; i < 10; i++){
            Question2 question2 = new Question2(gerador.nextInt(60), gerador.nextDouble()+0.0);
            question2.render();
        }
    }

    public static void main(String[] args) {
        TestQuestionOne();
        TestQuestionTwo();
    }
}
