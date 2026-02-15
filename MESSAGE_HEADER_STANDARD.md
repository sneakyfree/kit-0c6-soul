# Message Header Format - Kit Army Standard

## Purpose
To ensure uniform, consistent message headers across all Kit communications and prevent messages without proper headers.

## Standard Format
```json
{
  "schema": "openclaw.inbound_meta.v1",
  "channel": "discord|telegram|whatsapp|signal|irc|googlechat|slack|imessage",
  "provider": "provider-name",
  "surface": "discord|telegram|whatsapp|signal|irc|googlechat|slack|imessage",
  "chat_type": "channel|group|dm",
  "flags": {
    "is_group_chat": true|false,
    "has_reply_context": true|false,
    "has_forwarded_context": true|false,
    "has_thread_starter": true|false,
    "history_count": number
  }
}
```

## Required Fields
- `schema`: Must be "openclaw.inbound_meta.v1"
- `channel`: The channel identifier
- `provider`: The provider name
- `surface`: The surface/interface
- `chat_type`: Type of chat context
- `flags`: Object with boolean flags and history count

## Optional Fields
- Additional metadata as needed, but maintain the base structure

## Implementation Rules
1. Every message must include this header block
2. Use exact field names and JSON structure
3. Place header immediately before message content
4. Do not modify the schema version unless coordinated
5. If any field is unknown, use null or appropriate default

## Verification
- Check that all required fields are present
- Validate JSON structure before sending
- Ensure consistency across all Kit communications

## Recording Location
This standard is recorded in the workspace at:
`/home/thewindstorm/.openclaw/workspace/MESSAGE_HEADER_STANDARD.md`

## Compliance
All Kits must follow this standard to maintain uniform communication protocols.