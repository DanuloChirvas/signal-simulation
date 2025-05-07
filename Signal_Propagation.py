def signal_propagation_simulation():
    test_data = [
        [
            "2",
            "Alpha 1 1 2 2",
            "Beta 3 1 4 2"
        ]
    ]

    case_num = 1
    for data in test_data:
        c = int(data[0])
        countries = []
        for i in range(1, c + 1):
            parts = data[i].split()
            name = parts[0]
            xl, yl, xh, yh = map(int, parts[1:])
            countries.append((name, xl, yl, xh, yh))

       
        max_x = max(xh for _, xl, _, xh, _ in countries)
        max_y = max(yh for _, xl, yl, xh, yh in countries)

        grid = [[None for _ in range(max_y + 2)] for _ in range(max_x + 2)]
        for idx, (_, xl, yl, xh, yh) in enumerate(countries):
            for x in range(xl, xh + 1):
                for y in range(yl, yh + 1):
                    grid[x][y] = idx

        motifs = len(countries)
        signal = [[[0] * motifs for _ in range(max_y + 2)] for _ in range(max_x + 2)]
        for idx, (_, xl, yl, xh, yh) in enumerate(countries):
            for x in range(xl, xh + 1):
                for y in range(yl, yh + 1):
                   
                    signal[x][y][idx] = 1_000_000.0

        done = [None] * motifs
        days = 0
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def check_country(idx):
            _, xl, yl, xh, yh = countries[idx]
            for x in range(xl, xh + 1):
                for y in range(yl, yh + 1):
                    if any(signal[x][y][m] == 0 for m in range(motifs)):
                        return False
            return True

        while True:
            for idx in range(motifs):
                if done[idx] is None and check_country(idx):
                    done[idx] = days

            if all(x is not None for x in done):
                break

            spread = [[[0] * motifs for _ in range(max_y + 2)] for _ in range(max_x + 2)]
            for x in range(1, max_x + 1):
                for y in range(1, max_y + 1):
                    if grid[x][y] is None:
                        continue
                    for m in range(motifs):
                        amount = signal[x][y][m] // 1000
                        if amount > 0:
                            for dx, dy in neighbors:
                                nx, ny = x + dx, y + dy
                                if grid[nx][ny] is not None:
                                    spread[nx][ny][m] += amount
                                    spread[x][y][m] -= amount

            for x in range(1, max_x + 1):
                for y in range(1, max_y + 1):
                    if grid[x][y] is None:
                        continue
                    for m in range(motifs):
                        signal[x][y][m] += spread[x][y][m]

           
            days =+ 1

        result = [(countries[i][0], done[i]) for i in range(motifs)]
        result.sort(key=lambda x: (x[1], x[0]))

        print(f"Case Number {case_num}")
        for name, d in result:
            print(f"{name} {d}")
        case_num += 1

signal_propagation_simulation()
