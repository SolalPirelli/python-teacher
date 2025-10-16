import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Function, FunctionExample, GuessResult

FUNCTION = Function(
  "returns the remainder from dividing its input by 3",
  ["x"],
  [[0], [1], [8], [-1], [-11]],
  "x % 3"
)
EXAMPLES = [FunctionExample(inputs, FUNCTION.evaluate(inputs)) for inputs in FUNCTION.sample_inputs]

def index(request):
    """
    Index HTML page, with `function` and `examples` for the template.
    """
    return render(request, 'hello_azure/index.html', {'function': FUNCTION, 'examples': EXAMPLES})

@csrf_exempt
def evaluate(request):
    """
    Input: POST with code as the request body
    Output: JSON with a 'result' string property, and:
    * If 'result' is 'correct', nothing else
    * If 'result' is 'incorrect', a 'sample' string containing information about a failing sample.
    * Otherwise, an 'error' string containing error details.
    """
    if request.method == 'POST':
        code = request.body
        (result, sample, error) = FUNCTION.guess_samples(code)
        if result == GuessResult.CORRECT:
          data = json.dumps({'result': 'correct'})
        elif result == GuessResult.INCORRECT:
          data = json.dumps({'result': 'incorrect', 'sample': ", ".join([str(i) for i in sample])})
        else:
          data = json.dumps({'result': 'error', 'error': error})
        return HttpResponse(data, content_type='application/json')
    return HttpResponseBadRequest()
