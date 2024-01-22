def all_permutations(elements):
    def generate_permutations_backtracking(input_list, output_list, result):
        if not input_list:
            result.append(output_list.copy())
            return

        for i in range(len(input_list)):
            new_output = output_list + [input_list[i]]
            remaining_input = input_list[:i] + input_list[i+1:]
            generate_permutations_backtracking(remaining_input, new_output, result)

    result = []
    generate_permutations_backtracking(elements, [], result)
    return result