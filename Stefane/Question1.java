
public class Question1 {

    private enum SituacaoFinal {
        APROVADO("aprovado"), REPROVADO("reprovado"), RECUPERACAO("recuperação");

        private String descricao;

        SituacaoFinal(String descricao){
            this.descricao = descricao;
        }

        public String getDescricao(){
            return descricao;
        }
    }

    private String nomeAluno;

    private Double notaFinal;

    private Double mediaEscolar = 5.0;

    private SituacaoFinal situacaoFinal;

    private static Double calcMedia(Double... notas){
       return ((notas[0]*2 + notas[1]*3 + notas[2]*5)/10);
    }

    public void processSituacaoFinal(){
        if(notaFinal >= mediaEscolar){
            situacaoFinal = SituacaoFinal.APROVADO;
        } else 
            if(notaFinal < mediaEscolar && notaFinal >= 3){
            situacaoFinal = SituacaoFinal.RECUPERACAO;  
        } else 
            if(notaFinal < 3){
            situacaoFinal = SituacaoFinal.REPROVADO;
        }
    }

    public void setNotaFinal(Double... notas){
        this.notaFinal = calcMedia(notas[0], notas[1], notas[2]);
    }

    public void render(){
        System.out.println("======= Resultado Final de "+ nomeAluno +" ======= ");
        System.out.println("Nota: "+notaFinal);
        System.out.println("Situação: "+ situacaoFinal.getDescricao());
    }

    public Question1(String nomeInicializado, Double... notas){
        this.nomeAluno = nomeInicializado;
        setNotaFinal(notas[0], notas[1], notas[2]);
        processSituacaoFinal();
    }
    
}
