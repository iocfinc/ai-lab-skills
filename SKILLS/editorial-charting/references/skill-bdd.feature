Feature: Editorial charting skill behavior
  The skill should help agents produce clear, maintainable editorial charts.

  Scenario: Agent creates an emphasis chart brief
    Given a user asks for a chart with one main takeaway
    When the agent uses the editorial-charting skill
    Then the agent states one chart claim
    And the agent selects a chart pattern from chart-patterns.yaml
    And the agent uses one hue plus shade levels from color-system.yaml

  Scenario: Agent avoids copying publication-specific style
    Given a user asks for an Economist-like chart
    When the agent uses the editorial-charting skill
    Then the agent applies editorial chart discipline
    And the agent avoids claiming to reproduce a proprietary style guide

  Scenario: Maintainer changes chart behavior
    Given a maintainer changes chart selection, color rules, or output contract
    When the maintainer updates the skill
    Then the maintainer updates the PRD, ADR, BDD, or WTF reference that explains the changed intent

  Scenario: Legacy skill path is invoked
    Given a user invokes economist-chart-editor
    When the agent reads the legacy skill
    Then the agent is directed to editorial-charting
    And the agent receives a minimal fallback workflow if the new skill is unavailable

  Scenario: Human or agent needs to choose a chart capability
    Given a user wants to understand what chart types the skill supports
    When the agent uses the editorial-charting skill
    Then the agent points to assets/contact-sheet.html
    And the agent can point repository reviewers to assets/contact-sheet-preview.png
    And the agent uses references/contact-sheet-setup.md for opening, printing, or rebuilding the sheet

  Scenario: Maintainer adds a new chart card
    Given a maintainer adds a new contact sheet card
    When the maintainer updates the skill
    Then the maintainer mirrors metadata in contact-sheet-capabilities.yaml
    And the maintainer rebuilds assets/contact-sheet.html with scripts/build_contact_sheet.py
    And the maintainer rebuilds assets/contact-sheet-preview.png with scripts/build_contact_sheet_preview.py when Pillow is available
    And the maintainer runs the checks in contact-sheet-review-rubric.yaml

  Scenario: Reviewers flag contact sheet issues
    Given a proofreader or visual creative director flags a contact sheet issue
    When the maintainer accepts the finding
    Then the maintainer updates the generator, contact sheet metadata, setup guide, or BDD scenarios as needed
    And the regenerated contact sheet reflects the accepted feedback
