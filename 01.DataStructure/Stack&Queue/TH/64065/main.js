function solution(s) {
  const arr = JSON.parse(s.replace(/{|}/g, (c) => (c === '{' ? '[' : ']'))).sort(
    (a, b) => a.length - b.length
  );
  let que = arr.shift();

  while (arr.length) {
    const items = arr.shift();
    const target = items.filter((x) => !que.includes(x));
    que = [...que, ...target];
  }

  return que;
}
