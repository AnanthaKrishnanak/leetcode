/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    xcopy = x

    if (x < 0) {
        return false
    }

    if (x < 10) {
        return true
    }

    let rev = 0

    while (x > 0) {
        var rem = x % 10 // gives last digit
        x = Math.floor(x / 10) // removes last digit
        rev = (rev * 10) + rem

    }

    return rev === xcopy

};
console.log(isPalindrome(121)) // true
console.log(isPalindrome(-121)) // false
console.log(isPalindrome(10)) // false
console.log(isPalindrome(-101)) // false