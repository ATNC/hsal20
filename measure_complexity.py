import random
import time

from bbst import BBST


def generate_random_dataset(size):
    return [random.randint(0, 10000) for _ in range(size)]


def measure_complexity():
    sizes = [100, 500, 1000]
    num_datasets = 100

    for size in sizes:
        total_insert_time = 0
        total_delete_time = 0
        total_search_time = 0

        for _ in range(num_datasets):
            dataset = generate_random_dataset(size)

            avl_tree = BBST()

            start_time = time.time()
            for key in dataset:
                avl_tree.insert(key)
            total_insert_time += time.time() - start_time

            start_time = time.time()
            for key in dataset:
                avl_tree.delete(key)
            total_delete_time += time.time() - start_time

            for key in dataset:
                avl_tree.insert(key)

            start_time = time.time()
            for key in dataset:
                avl_tree.find(key)
            total_search_time += time.time() - start_time

        avg_insert_time = total_insert_time / num_datasets
        avg_delete_time = total_delete_time / num_datasets
        avg_search_time = total_search_time / num_datasets

        print(f"Dataset size: {size}")
        print(f"Avg. Insert Time: {avg_insert_time:.6f} seconds")
        print(f"Avg. Delete Time: {avg_delete_time:.6f} seconds")
        print(f"Avg. Search Time: {avg_search_time:.6f} seconds")
        print()


measure_complexity()
