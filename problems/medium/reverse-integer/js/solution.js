
/**
 * @param {number} x
 * @return {number}
 */

var reverse = function (x) {
    const actualx = x
    x = Math.abs(x)
    let rev = 0

    while (x > 0) {
        var rem = x % 10
        x = Math.floor(x / 10)
        rev = (rev * 10) + rem

    }

    if(rev > 2**31 || rev < (2**31)* -1){
        return 0
    }

    return actualx > 0 ? rev : rev * -1

};


console.log(reverse(123)) // 321
console.log(reverse(-123)) // -321
console.log(reverse(120)) // 21
console.log(reverse(0)) // 0