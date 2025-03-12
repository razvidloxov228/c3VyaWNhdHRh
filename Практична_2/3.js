let a = "5";
let b = "13cvb";
let c = "12.9sxdcfgv";
a = Number(a);
b = parseInt(b.match(/\d+/)[0]);
c = parseFloat(c.match(/[\d.]+/)[0]);
console.log(`a ${a} ${typeof a}`);
console.log(`b ${b} ${typeof b}`);
console.log(`b ${c} ${typeof c}`);
