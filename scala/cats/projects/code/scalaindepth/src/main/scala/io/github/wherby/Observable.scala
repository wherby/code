package io.github.wherby
import scala.language.reflectiveCalls
/** Defines a trait that marks a class as allowing external
 * viewers to be notified of changes.
 */
trait Observable {
  // Defines a type returned when registering a callback.
  type Handle <: {
    def remove() : Unit
  }
  /** registered callbacks for this observable */
  protected var callbacks = Map[Handle, this.type => Unit]()

  /** Registers a new observer on this class.
   * Observers are simple functions that take the class and
   * return nothing.   A handle is returned that allows
   * the observer to deregister from this observable.
   */
  def observe(callback : this.type => Unit) : Handle = {
    val handle = createHandle(callback)
    callbacks += (handle -> callback)
    handle
  }
  /** Removes an observer from this class. */
  def unobserve(handle : Handle) : Unit = {
    callbacks -= handle
  }
  /** This method is called by subclasses upon state change to
   * notify listeners of the change.
   */
  protected def notifyListeners() : Unit =
    for(callback <- callbacks.values) callback(this)

  /**
   * Subclasses override this to provide their own callback disambiguation scheme.
   */
  protected def createHandle(callback : this.type => Unit) : Handle
}

/** This trait provides a default implementation
 * for the handlers type. */
trait DefaultHandles extends Observable {
  /** A simple handle implementation */
  class HandleClass {
    def remove() ={
      DefaultHandles.this.unobserve(this)
    }
  }
  type Handle = HandleClass
  /** Every callback is assigned a new handle. */
  protected def createHandle(callback : this.type => Unit) : Handle = new HandleClass
}


/** This defines a basic store or cache of a single value type.
 * This store is observable and will notify listeners when the stored
 * value is changed.
 */
class VariableStore[X](private var value : X) extends Observable with DefaultHandles {
  /** Retreive the stored value */
  def get : X = value
  /** Sets the stored value.  Will notify observers */
  def set(newValue : X) : Unit = {
    value = newValue
    notifyListeners()
  }
  // Overridden for pretty REPL usage.
  override def toString : String = "VariableStore(" + value + ")"
}

/** This trait defines a mechanism for managing handles from
 * observerables such that they can all be unregistered when
 * the current class is 'finished'
 */
trait Dependencies {
  // This type allows us to refer to any handle from any
  // observable.  Because handle is defined inside the Observable
  // we use an existential for the actual Observable.
  type Ref = x.Handle forSome { val x: Observable }
  /** The current registered observers. */
  var handles = List[Ref]()
  /** Adds a new handle to manage */
  def addHandle(handle : Ref) : Unit = {
    handles :+= handle
  }
  /** Removes all observers using the registrered handles */
  def removeDependencies() ={
    for(h <- handles) h.remove()
    handles = List()
  }
  /** This method mimics Observable.observe except that it registers
   * an observer *and* adds it to the dependency list.
   */
  protected def observe[T <: Observable](obj : T)(handler : T => Unit) : Ref = {
    val ref = obj.observe(handler)
    addHandle(ref)
    ref
  }
}
