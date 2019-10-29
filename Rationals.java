/**
   This class provides common arithmetic operations for a rational
   numbers (integer numerator and denominator) ADT.

   All rational numbers are maintained in lowest terms, with a
   denominator that is a positive integer.

   @see java.lang.Object
   @author YOUR NAME HERE
   @date January 2018
*/


public class Rational {
    // TODO
    private int num, den;
    /**
       Default constructor initializes rational to 0.
    */
    public Rational() {
        this.num = 0;
        this.den = 1;
	//TODO
    }


    /**
       <code>Rational</code> constructor
       @param num the numerator
       @param den the denominator
       @throws NumberFormatException if den is zero
    */
    public Rational(int num, int den) {
    // TODO
        if(den == 0){
            den = 1;
            throw new NumberFormatException("Denominator can't be 0");
        } else if(den < 0){
            den = den*-1;
            num = num*-1;
        }
        this.num = num;
        this.den = den;
        this.reduce();
    }

    /** 
	private function GCD, not provided to clients
	finds the greatest common divisor of M and N
	Pre: M and N are defined
	Post: returns the GCD of M and N, by Euclid's Algorithm
    */
    private int GCD(int m, int n) {
        int r = m%n;
        while(r!=0){
            m = n;
            n = r;
            r = m%n;
        }
	    return n;
    }

    /** 
	private function reduce, not provided to clients
	reduces a rational
	Pre: r is a rational
	Post: returns the reduced rational
    */
    private void reduce() {
        int gcd = this.GCD(this.num, this.den);
        this.num = this.num/gcd;
        this.den =  this.den/gcd;
        if(this.den < 0){
            this.den = this.den*-1;
            this.num = this.num*-1;
        }
    }

    /** 
	@param R a rational
	@return true iff rational object < R.
    */

    public boolean lt(Rational R) {
    // TODO
        // int num1 = this.num * R.den;
        // int num2 = R.num * this.den;
        // return num1 < num2;
        this.reduce();
        R.reduce();
        return (this.num * R.den) < (R.num * this.den);
    }

    /** 
	@param R a rational
	@return true iff rational object > R.
    */

    public boolean gt(Rational R) {
        // TODO
        this.reduce();
        R.reduce();
        return (this.num * R.den) > (R.num * this.den);
    }

    /** 
	@param R a rational
	@return true iff rational object = R.
    */

    public boolean equals(Rational R) {
        // TODO
        this.reduce();
        R.reduce();
        return (this.num * R.den) == (R.num * this.den);
    }

    /** 
	@param r
	@param s
	@return Rational corresponding to sum of r + s.
    */
    public static Rational add(Rational r, Rational s) {
    // TODO
        int num1 = r.num * s.den;
        int num2 = s.num * r.den;
        int den = r.den * s.den;
        Rational result = new Rational(num1+num2, den);
        result.reduce();
        return result;
	    // return new Rational(num1+num2, den);
    }

    /** 
	@param r
	@param s
	@return Rational corresponding to difference of r - s.
    */
    public static Rational subtract(Rational r, Rational s) {
        // TODO
        int num1 = r.num * s.den;
        int num2 = s.num * r.den;
        int den = r.den * s.den;
        Rational result = new Rational(num1-num2, den);
        result.reduce();
        return result;
        // return new Rational(num1-num2, den);
    }

    /** 
	@param r
	@param s
	@return Rational corresponding to product of r * s.
    */
    public static Rational multiply(Rational r, Rational s) {
        // TODO
        int num = r.num * s.num;
        int den = r.den * s.den;
        Rational result = new Rational(num, den);
        result.reduce();
        return result;
        // return new Rational(num, den);
    }

    /** 
	Convert to String in standard format (i.e., numerator/denominator)
	@ return a <code>String</code> representation of
	the item.
    */
    public String toString() {
    //TODO
	    return this.num+"/"+this.den;
    }


}  // end of Rational class
