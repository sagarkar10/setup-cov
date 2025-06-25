
#!/bin/bash
set -e

# Define module list
modules=("common" "services/service1" "services/service2")

for module in "${modules[@]}"; do
  echo "Running tests for $module"

  src_path="$module/src"
  test_path="$module/tests"
  html_report_path="$module/htmlcov"
  xml_report_path="$module/cov.xml"

  PYTHONPATH=. pytest \
    --cov="$src_path" \
    --cov-report=term \
    --cov-report="html:$html_report_path" \
    --cov-report="xml:$xml_report_path" \
    "$test_path"
done

