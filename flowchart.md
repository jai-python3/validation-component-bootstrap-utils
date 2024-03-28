:::mermaid
graph TD;
  A[Start] --> B[_init_templating_system];
  B --> C[generate_validation_module];
  C --> D{"extension == .csv"};
  D -->|Yes| E["_generate_validation_modules_for_tsv_file"];
  D -->|No| F{"extension == .tsv or\n extension == .txt"};
  F --> |Yes| E["_generate_validation_modules_for_tsv_file"];
  F -->|No| G[Unsupported exception];
  E --> H[_derive_column_headers_for_tsv_file];


:::
