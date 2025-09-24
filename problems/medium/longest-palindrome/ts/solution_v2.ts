function checkIsPalindrome(subString: string): boolean {
  let i = 0,
    l = subString.length - 1;
  while (i < l) {
    if (subString[i] !== subString[l]) {
      return false;
    }
    i++;
    l--;
  }
  return true;
}

function longestPalindrome(s: string): string {
  let result = "";
  const cache = new Map();

  let left = 0,
    right = s.length;

  while (left < s.length) {
    right = s.length;
    while (left < right) {
      const subString = s.slice(left, right);

      if (result.length > subString.length) {
        break;
      }

      let isPalindrome = cache.get(subString);

      if (isPalindrome === undefined) {
        isPalindrome = checkIsPalindrome(subString);
        cache.set(subString, isPalindrome);
      }

      if (isPalindrome) {
        result = result.length > subString.length ? result : subString;
      }

      right--;
    }
    left++;
  }

  return result;
}

