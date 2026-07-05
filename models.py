from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    raw_input: str
    stories: List[str]
    current_index: int
    analyses: List[dict]
    final_report_md: Optional[str]
    final_report_json: Optional[dict]