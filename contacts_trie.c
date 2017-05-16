// SEE THE SPEC AT https://www.hackerrank.com/challenges/ctci-contacts
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

#define LETTERS 26

// ### TYPEDEFS ###
typedef struct LetterTrie
{
    unsigned int children;
    unsigned int terminations;
    struct LetterTrie *Next[LETTERS];
} LetterTrie;

// ### PROTOTYPES ###
int ASCII_to_index(const char chr);
bool Create_Word(const char *word, LetterTrie *TrieTrunk);
unsigned int Check(const char *word, LetterTrie *TrieTrunk);
unsigned int Delete_Trie(LetterTrie *Trie);

// ### IMPLEMENTATION ###
int ASCII_to_index(const char chr) {
    return tolower(chr) - 'a';
}

bool Create_Word(const char *word, LetterTrie *TrieTrunk) {
    \\ Add a word to the TrieTrunk.
    
    LetterTrie *Trie = TrieTrunk;
    
    for(int chr = 0;; chr++) {
        if (word[chr] != '\0') {
            ++(Trie->children);
            int Index = ASCII_to_index(word[chr]);
            if (!Trie->Next[Index]) {
                Trie->Next[Index] = calloc(1,sizeof(LetterTrie));
            }
            Trie = Trie->Next[Index];
        } else {
            ++(Trie->terminations);
            return true;
        }
    }
}

unsigned int Delete_Trie(LetterTrie *Trie) {
    \\ Recursively free all the nodes in a LetterTrie.
    unsigned int failures = 0;
    
    for (int Index = 0; Index < LETTERS; Index++) {
        if (Trie->Next[Index] != NULL) {
            failures += Delete_Trie(Trie->Next[Index]);
        }
    }
 
    if (failures == 0) {
        free(Trie);
    }
    return failures;
}

unsigned int check(const char *word, LetterTrie *TrieTrunk) {
    \\ Return a count of contacts beginning with te given word
    LetterTrie *Trie = TrieTrunk;

    for (int iter = 0; ; iter++)
    {
        if (word[iter] == '\0') {
            return Trie->children + Trie->terminations;
        } else {
            int Index = ASCII_to_index(word[iter]);
            if (Trie->Next[Index] != NULL) {
                Trie = Trie->Next[Index];
            } else {
                return 0;
            }
        }
    }
}

int main(void) {
    \\ Perform n operations of add or find on a LetterTrie
    int n;
    LetterTrie *TrieTrunk = calloc(1, sizeof(LetterTrie));
    scanf("%d",&n);
    
    for(int i = 0; i < n; i++) {
        char* op = (char *)malloc(512000 * sizeof(char));
        char* contact = (char *)malloc(512000 * sizeof(char));
        scanf("%s %s",op,contact);
        if (strcmp(op, "add") == 0) {
            Create_Word(contact, TrieTrunk);
        } else if (strcmp(op, "find") == 0) {
            int count = check(contact, TrieTrunk);
            printf("%i\n", count);
        }
        free(op);
        free(contact);
    }
    
    return Delete_Trie(TrieTrunk);
}
