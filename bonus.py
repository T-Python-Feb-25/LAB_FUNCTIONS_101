def generate_pattern(n: int) -> str:
    result = []
    result.append("✨ Number Pattern ✨\n")
    for i in range(n, 0, -1):
        line = ' '.join(str(x) for x in range(i, 0, -1))
        result.append(f"🌟 {line} 🌟")
    return '\n'.join(result)

pattern = generate_pattern(5)
print(pattern) 