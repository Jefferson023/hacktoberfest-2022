import java.util.Scanner

fun main() {
    val read = Scanner(System.`in`)
    
    val workedHours: Int = read.nextInt()
	val baseSalaryByHours: Float = read.nextFloat()
	println(monthlySalary(workedHours, baseSalaryByHours))
}

fun monthlySalary(workedHours: Int, baseSalaryByHours: Float) : Float{
    return if (workedHours < 40) 0f else (workedHours-40)*baseSalaryByHours + baseSalaryByHours*40 
}