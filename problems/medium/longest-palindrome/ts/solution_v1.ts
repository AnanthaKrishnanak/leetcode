//First working solution

function isPalindrome(subString: string): boolean {
  let reverse = "";
  let l = subString.length - 1;
  while (l >= 0) {
    reverse += subString[l];
    l--;
  }
  return reverse === subString;
}

function longestPalindrome(s: string): string {
  const results: string[] = [];

  let left = 0,
    right = s.length;

  while (left < s.length) {
    right = s.length;
    while (left < right) {
      const subString = s.slice(left, right);
      if (isPalindrome(subString)) {
        results.push(subString);
      }
      right--;
    }
    left++;
    right--;
  }

  const sorted = results.sort((a, b) => a.length - b.length);

  return sorted[sorted.length - 1];
}

testCases.forEach((testCase) => {
  console.log({
    input: testCase.input,
    result: longestPalindrome(testCase.input),
    actualResult: testCase.output,
  });
});
