const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout
})
function printRLE(str) {
    let result = ""
    let n = str.length;
    for (let i = 0; i < n; i++) {
       // Count occurrences of current character
       let count = 1;
       while (i < n - 1 && str[i] == str[i + 1]) {
count++;
i++; }
       // character and its count
       result += str[i] + count
    }
    console.log("\n",result)
}
readline.question("Enter a string:\n", str => {
    printRLE(str);
    readline.close()
})
