import java.util.Scanner

fun main() {
    
    val read = Scanner(System.`in`)
    
    val value1: Int = read.nextInt()
	val value2: Int = read.nextInt()
	val value3: Int = read.nextInt()
	println(mean(value1, value2, value3))
}

fun mean(value1: Int, value2: Int, value3:Int) : Float{
    return (value1*2 + value2*3 + value3*5)/10f
}