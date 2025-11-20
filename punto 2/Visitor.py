from Gramatica_matricesVisitor import Gramatica_matricesVisitor
from Gramatica_matricesParser import Gramatica_matricesParser

class ExecVisitor(Gramatica_matricesVisitor):
    def __init__(self):
        self.mem = {}

    def visitProgram(self, ctx: Gramatica_matricesParser.ProgramContext):
        return self.visit(ctx.expr())

    def visitVar(self, ctx: Gramatica_matricesParser.VarContext):
        name = ctx.ID().getText()
        return self.mem[name]

    def visitMatrix(self, ctx: Gramatica_matricesParser.MatrixContext):
        result = []
        for r in ctx.row():
            row = [int(x.getText()) for x in r.INT()]
            result.append(row)
        return result

    def visitMulExpr(self, ctx: Gramatica_matricesParser.MulExprContext):
        A = self.visit(ctx.expr(0))
        B = self.visit(ctx.expr(1))
        a_rows, a_cols = len(A), len(A[0])
        b_rows, b_cols = len(B), len(B[0])
        if a_cols != b_rows:
            raise RuntimeError("Dimensiones incompatibles")
        return [[sum(A[i][k]*B[k][j] for k in range(a_cols)) for j in range(b_cols)] for i in range(a_rows)]

    def visitAddExpr(self, ctx: Gramatica_matricesParser.AddExprContext):
        A = self.visit(ctx.expr(0))
        B = self.visit(ctx.expr(1))
        return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def visitSubExpr(self, ctx: Gramatica_matricesParser.SubExprContext):
        A = self.visit(ctx.expr(0))
        B = self.visit(ctx.expr(1))
        return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def visitParExpr(self, ctx: Gramatica_matricesParser.ParExprContext):
        return self.visit(ctx.expr())
