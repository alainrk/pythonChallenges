function ex1(predators) {
    const adj = { "-1": [] }
    for (let i = 0; i < predators.length; i++) {
        if (predators[i] == -1) {
            adj["-1"].push(i)
            continue
        }
        if (!adj[predators[i]]) {
            adj[predators[i]] = []
        }
        adj[predators[i]].push(i)
    }

    const levels = {"-1": 0}
    const levelGroups = new Set()
    const marked = {"-1": true}
    const q = ["-1"]
    while (q.length) {
        const curr = q.shift()
        if (!adj[curr]) continue
        for (const n of adj[curr]) {
            if (!marked[n]) {
                marked[n] = true
                q.push(n)
                levels[n] = levels[curr] + 1
                levelGroups.add(levels[n])
            }
        }
    }
    return levelGroups.size
}

function ex2(keyTimes) {
    let slowest = { char: keyTimes[0][0], time: keyTimes[0][1] }
    let now = keyTimes[0][1]
    for (let i=1; i < keyTimes.length; i++) {
        const passed = keyTimes[i][1] - now
        if (passed > slowest.time) {
            slowest.char = keyTimes[i][0],
            slowest.time = passed
        }
        now = keyTimes[i][1]
    }
    return String.fromCharCode(97+parseInt(slowest.char))
}

function ex3(index, identity) {
    const arr = []
    for (let i=0; i<index.length; i++) {
        arr.splice(index[i], 0, identity[i])
    }
    return arr
}

