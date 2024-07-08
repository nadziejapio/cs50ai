import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for k, v in self.domains.items():
            to_delete = []
            for word in v:
                if len(word) != k.length:
                    to_delete.append(word)
            for i in to_delete:
                self.domains[k].remove(i)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        
        print('x', x, 'y', y)
        revised = False
        overlap = self.crossword.overlaps[x, y]
        if overlap:
            i, j = overlap
            to_remove = []
            for word_x in self.domains[x]:
                found = any(
                    word_x[i] == word_y[j] for word_y in self.domains[y]
                )
                if not found:
                    to_remove.append(word_x)
                    revised = True

            for word in to_remove:
                self.domains[x].remove(word)

        return revised
    
    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
    
        if arcs == None:
            arcs = []
            for i in self.domains:
                for j in self.crossword.neighbors(i):
                    if i != j:
                        arcs.append((i, j))
        print('arcs', arcs)             
        while arcs:
            arc = arcs[0]
            is_changed = self.revise(arc[0], arc[1])
            if is_changed:
                print('changed', arc[0])
                print('value', self.domains[arc[0]])
                if len(self.domains[arc[0]]) == 0:
                    return False
                for n in self.crossword.neighbors(arc[0]) - {arc[1]}:
                    arcs.append((n, arc[0]))
            arcs.remove(arcs[0])
        return True     

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # print('assigment_complete', assignment)
        
        for var in self.crossword.variables:
            if var not in assignment or not assignment[var]:
                return False
        return True             

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        
        words = [assignment.values()]
        if len(words) != len(set(words)):
            return False
        
        for v, w in assignment.items():
            if len(w) != v.length:
                return False
        for v in assignment:
            for v1 in assignment:
                if v != v1:
                    overlap = self.crossword.overlaps[v, v1]
                    if overlap:
                        i, j = overlap
                        if assignment[v][i] != assignment[v1][j]:
                            return False
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """

        print('var', var)
        print('asssigment', assignment)
        neighbors = self.crossword.neighbors(var) - set(assignment)
        print('neig', neighbors)
        ans = []
        for i in self.domains[var]:
            ans.append(i)
            print('neighbors', len(self.crossword.neighbors(var)))
        print('aaanss or', ans)
        return sorted(ans, key=lambda v: sum(1 for neighbor in neighbors if v in self.domains[neighbor]))

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        ans = []
        for k, v in self.domains.items():
            # if not fewest_var:
            #     fewest_var = k
            # print('k', k)
            # print('v', v)
            # print('fewest_var', fewest_var)
            if k not in assignment:
                ans.append(k)
                # return k
                # print('if self.domains[k]', self.domains[k], 'len', len(self.domains[k]), 'self domains[fewest_var]', self.domains[fewest_var], 'len', len(self.domains[fewest_var]))
                # if len(self.domains[k]) <= len(self.domains[fewest_var]):
                #     fewest_var = k
                #     print('changed fewest', fewest_var)
        print('fewewst', ans)
        fewer = ans[0]
        for a in ans:
            if len(self.domains[a]) < len(self.domains[fewer]):
                fewer = a
        return fewer     
            
    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """

        print('backtrack assignment', assignment)
        if self.assignment_complete(assignment):
            print('returning', assignment)
            return assignment
        
        var = self.select_unassigned_variable(assignment)
        print('var in back', var)
        for value in self.order_domain_values(var, assignment):
            print('vaaaar', var)
            print('value', value)
            print('asssss', assignment)
            assignment[var] = value
            if self.consistent(assignment):
                result = self.backtrack(assignment)
                if result != None:
                    return result
            del assignment[var]
            print('removed ass', assignment)
        return None
                
                
def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
