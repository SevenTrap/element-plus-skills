# form API — Element Plus 2.14.6

Adapted from [official 2.14.6 documentation](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/form.md) at `5ac2b162180d3922d77c50990bb40c2f02376796`.
Read this reference when exact prop types, defaults, events, slots, or exposes are needed. Version labels identify introductions; future removal notices do not add future APIs.

The documentation type badges are rendered as bold labels here; accompanying TypeScript signatures and unions retain their original meaning.

## Form API

### Form Attributes

| Name                              | Description                                                                                                                                                                                                                      | Type                                           | Default |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------- |
| model                             | Data of form component.                                                                                                                                                                                                          | **object**`Record<string, any>`                 | —       |
| rules                             | Validation rules of form.                                                                                                                                                                                                        | **object**`FormRules`                           | —       |
| inline                            | Whether the form is inline.                                                                                                                                                                                                      | **boolean**                                     | false   |
| label-position                    | Position of label. If set to `'left'` or `'right'`, `label-width` prop is also required.                                                                                                                                         | **enum**`'left' \| 'right' \| 'top'`            | right   |
| label-width                       | Width of label, e.g. `'50px'`. All its direct child form items will inherit this value. `auto` is supported.                                                                                                                     | **string** / **number**                          | ''      |
| label-suffix                      | Suffix of the label.                                                                                                                                                                                                             | **string**                                      | ''      |
| hide-required-asterisk            | Whether to hide required fields should have a red asterisk (star) beside their labels.                                                                                                                                           | **boolean**                                     | false   |
| require-asterisk-position         | Position of asterisk.                                                                                                                                                                                                            | **enum**`'left' \| 'right'`                     | left    |
| show-message                      | Whether to show the error message.                                                                                                                                                                                               | **boolean**                                     | true    |
| inline-message                    | Whether to display the error message inline with the form item.                                                                                                                                                                  | **boolean**                                     | false   |
| status-icon                       | Whether to display an icon indicating the validation result.                                                                                                                                                                     | **boolean**                                     | false   |
| validate-on-rule-change           | Whether to trigger validation when the `rules` prop is changed.                                                                                                                                                                  | **boolean**                                     | true    |
| size                              | Control the size of components in this form.                                                                                                                                                                                     | **enum**`'' \| 'large' \| 'default' \| 'small'` | —       |
| disabled                          | Whether to disable all components in this form. Before (since 2.12.0), if set to `true`, it will override the `disabled` prop of the inner component. After (since 2.12.0), the configuration of the internal components takes precedence. | **boolean**                                     | false   |
| scroll-to-error                   | When validation fails, scroll to the first error form entry.                                                                                                                                                                     | **boolean**                                     | false   |
| scroll-into-view-options (since 2.3.2) | When validation fails, it scrolls to the first error item based on the scrollIntoView option. [scrollIntoView](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView).                                         | **object**`ScrollIntoViewOptions` / **boolean**  | true    |

### Form Events

| Name     | Description                             | Type                                                                         |
| -------- | --------------------------------------- | ---------------------------------------------------------------------------- |
| validate | triggers after a form item is validated | **Function**`(prop: FormItemProp, isValid: boolean, message: string) => void` |

### Form Slots

| Name    | Description               | Subtags  |
| ------- | ------------------------- | -------- |
| default | customize default content | FormItem |

### Form Exposes

| Name                       | Description                                                                                          | Type                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| validate                   | Validate the whole form. Receives a callback or returns `Promise`.                                   | **Function**`(callback?: FormValidateCallback) => Promise<void>`                                                                   |
| validateField              | Validate specified fields.                                                                           | **Function**`(props?: Arrayable<FormItemProp> \| undefined, callback?: FormValidateCallback \| undefined) => FormValidationResult` |
| resetFields                | Reset specified fields and remove validation result.                                                 | **Function**`(props?: Arrayable<FormItemProp> \| undefined) => void`                                                               |
| scrollToField              | Scroll to the specified fields.                                                                      | **Function**`(prop: FormItemProp) => void`                                                                                         |
| clearValidate              | Clear validation messages for all or specified fields.                                               | **Function**`(props?: Arrayable<FormItemProp> \| undefined) => void`                                                               |
| fields (since 2.7.3)            | Get all fields context.                                                                              | **array**`FormItemContext[]`                                                                                                       |
| getField (since 2.10.2)         | Get a field context.                                                                                 | **Function**`(prop: FormItemProp) => FormItemContext \| undefined`                                                                 |
| setInitialValues (since 2.13.1) | Set initial values for form fields. When `resetFields` is called, fields will reset to these values. | **Function**`(initModel: Record<string, any>) => void`                                                                             |

## FormItem API

### FormItem Attributes

| Name                    | Description                                                                                                                                                            | Type                                                | Default |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ------- |
| prop                    | A key of `model`. It could be a path of the property (e.g `a.b.0` or `['a', 'b', '0']`). In the use of `validate` and `resetFields` method, the attribute is required. | **string** / **string&#91;&#93;**                     | —       |
| label                   | Label text.                                                                                                                                                            | **string**                                           | —       |
| label-position (since 2.7.7) | Position of item label. If set to `'left'` or `'right'`, `label-width` prop is also required. Default extend `label-position` of `form`.                               | **enum**`'left' \| 'right' \| 'top'`                 | ''      |
| label-width             | Width of label, e.g. `'50px'`. `'auto'` is supported.                                                                                                                  | **string** / **number**                               | —       |
| required                | Whether the field is required or not, will be determined by validation rules if omitted.                                                                               | **boolean**                                          | —       |
| rules                   | Validation rules of form, see the [following table](https://github.com/element-plus/element-plus/blob/2.14.6/docs/en-US/component/form.md#formitemrule), more advanced usage at [async-validator](https://github.com/yiminghe/async-validator).             | **object**`Arrayable<FormItemRule>`                  | —       |
| error                   | Field error message, set its value and the field will validate error and show this message immediately.                                                                | **string**                                           | —       |
| show-message            | Whether to show the error message.                                                                                                                                     | **boolean**                                          | true    |
| inline-message          | Inline style validate message.                                                                                                                                         | **boolean**                                          | false   |
| size                    | Control the size of components in this form-item.                                                                                                                      | **enum**`'' \| 'large' \| 'default' \| 'small'`      | —       |
| for                     | Same as for in native label.                                                                                                                                           | **string**                                           | —       |
| validate-status         | Validation state of formItem.                                                                                                                                          | **enum**`'' \| 'error' \| 'validating' \| 'success'` | —       |

#### FormItemRule

| Name    | Description                     | Type                        | Default |
| ------- | ------------------------------- | --------------------------- | ------- |
| trigger | How the validator is triggered. | **enum**`'blur' \| 'change'` | —       |

> **Tip** 

If you don't want to trigger the validator based on input events, set the `validate-event` attribute as `false` on the corresponding input type components (`<el-input>`, `<el-radio>`, `<el-select>`, ...).


### FormItem Slots

| Name    | Description                                   | Type                         |
| ------- | --------------------------------------------- | ---------------------------- |
| default | Content of Form Item.                         | —                            |
| label   | Custom content to display on label.           | **object**`{ label: string }` |
| error   | Custom content to display validation message. | **object**`{ error: string }` |

### FormItem Exposes

| Name                      | Description                                                                                        | Type                                                                                                 |
| ------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| size                      | Form item size.                                                                                    | **object**`ComputedRef<'' \| 'large' \| 'default' \| 'small'>`                                        |
| validateMessage           | Validation message.                                                                                | **object**`Ref<string>`                                                                               |
| validateState             | Validation state.                                                                                  | **object**`Ref<'' \| 'error' \| 'validating' \| 'success'>`                                           |
| validate                  | Validate form item.                                                                                | **Function**`(trigger: string, callback?: FormValidateCallback \| undefined) => FormValidationResult` |
| resetField                | Reset current field and remove validation result.                                                  | **Function**`() => void`                                                                              |
| clearValidate             | Remove validation status of the field.                                                             | **Function**`() => void`                                                                              |
| setInitialValue (since 2.13.1) | Set initial value for this field. When `resetField` is called, the field will reset to this value. | **Function**`(value: any) => void`                                                                    |

## Type Declarations

<details>
  <summary>Show declarations</summary>

```ts
type Arrayable<T> = T | T[]

type FormValidationResult = Promise<boolean>

// ValidateFieldsError: see [async-validator](https://github.com/yiminghe/async-validator/blob/master/src/interface.ts)
type FormValidateCallback = (
  isValid: boolean,
  invalidFields?: ValidateFieldsError
) => Promise<void> | void

// RuleItem: see [async-validator](https://github.com/yiminghe/async-validator/blob/master/src/interface.ts)
interface FormItemRule extends RuleItem {
  trigger?: Arrayable<string>
}

type Primitive = null | undefined | string | number | boolean | symbol | bigint
type BrowserNativeObject = Date | FileList | File | Blob | RegExp
type IsTuple<T extends ReadonlyArray<any>> = number extends T['length']
  ? false
  : true
type ArrayMethodKey = keyof any[]
type TupleKey<T extends ReadonlyArray<any>> = Exclude<keyof T, ArrayMethodKey>
type ArrayKey = number
type PathImpl<K extends string | number, V> = V extends
  Primitive | BrowserNativeObject
  ? `${K}`
  : `${K}` | `${K}.${Path<V>}`
type Path<T> =
  T extends ReadonlyArray<infer V>
    ? IsTuple<T> extends true
      ? {
          [K in TupleKey<T>]-?: PathImpl<Exclude<K, symbol>, T[K]>
        }[TupleKey<T>]
      : PathImpl<ArrayKey, V>
    : {
        [K in keyof T]-?: PathImpl<Exclude<K, symbol>, T[K]>
      }[keyof T]
type FieldPath<T> = T extends object ? Path<T> : never
// MaybeRef: see [@vueuse/core](https://github.com/vueuse/vueuse/blob/main/packages/shared/utils/types.ts)
// UnwrapRef: see [vue](https://github.com/vuejs/core/blob/main/packages/reactivity/src/ref.ts)
type FormRules<T extends MaybeRef<Record<string, any> | string> = string> =
  Partial<
    Record<
      UnwrapRef<T> extends string ? UnwrapRef<T> : FieldPath<UnwrapRef<T>>,
      Arrayable<FormItemRule>
    >
  >

type FormItemValidateState = (typeof formItemValidateStates)[number]
type FormItemProps = ExtractPropTypes<typeof formItemProps>

type FormItemContext = FormItemProps & {
  $el: HTMLDivElement | undefined
  size: ComponentSize
  validateMessage: string
  validateState: FormItemValidateState
  isGroup: boolean
  labelId: string
  inputIds: string[]
  hasLabel: boolean
  fieldValue: any
  propString: string
  addInputId: (id: string) => void
  removeInputId: (id: string) => void
  validate: (
    trigger: string,
    callback?: FormValidateCallback
  ) => FormValidationResult
  resetField(): void
  clearValidate(): void
  setInitialValue: (value: any) => void
}
```

</details>
