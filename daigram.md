---
config:
  layout: fixed
---
flowchart TD
 subgraph subGraph0["Data Retrieval & Processing"]
        B{"Microsoft Graph API"}
        C["PowerShell Script"]
        D["Microsoft Graph API Query"]
        E["Intune Data ﬂ°°40¶ßMultiple Resourcesﬂ°°41¶ß"]
        F{"Data Filtering & Formatting"}
        G["Custom Report ﬂ°°40¶ßVarious Formatsﬂ°°41¶ß"]
  end
 subgraph Distribution["Distribution"]
        H{"Distribution"}
        I["Email"]
        J["Shared Location"]
        K["Scheduled Task"]
  end
    A["Intune Environment"] --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I & J & K
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#cfc,stroke:#333,stroke-width:2px
    style D fill:#eee,stroke:#333,stroke-width:1px
    style E fill:#eee,stroke:#333,stroke-width:1px
    style F fill:#eee,stroke:#333,stroke-width:1px
    style G fill:#eee,stroke:#333,stroke-width:1px
    style H fill:#eee,stroke:#333,stroke-width:1px
    style I fill:#eee,stroke:#333,stroke-width:1px
    style J fill:#eee,stroke:#333,stroke-width:1px
    style K fill:#eee,stroke:#333,stroke-width:1px
